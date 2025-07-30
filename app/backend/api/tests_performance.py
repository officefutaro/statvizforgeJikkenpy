"""
API v2.0 パフォーマンステスト
レスポンス時間、負荷耐性、メモリ使用量などを測定
"""

from django.test import TestCase, Client
from django.urls import reverse
import time
import json
import statistics
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import psutil
import os


class ResponseTimeTest(TestCase):
    """レスポンス時間測定テスト"""
    
    def setUp(self):
        self.client = Client()
        self.endpoints = [
            '/api/v1/projects/',
            '/api/v1/server-info/',
            '/api/v1/test/',
        ]
    
    def test_single_request_response_time(self):
        """単一リクエストのレスポンス時間テスト"""
        results = {}
        
        for endpoint in self.endpoints:
            response_times = []
            
            # 各エンドポイントを10回テスト
            for _ in range(10):
                start_time = time.perf_counter()
                response = self.client.get(endpoint)
                end_time = time.perf_counter()
                
                response_time = end_time - start_time
                response_times.append(response_time)
                
                # ステータスコードが正常範囲内
                self.assertIn(response.status_code, [200, 404])
            
            # 統計情報を計算
            avg_time = statistics.mean(response_times)
            max_time = max(response_times)
            min_time = min(response_times)
            
            results[endpoint] = {
                'average': avg_time,
                'max': max_time,
                'min': min_time,
                'samples': len(response_times)
            }
            
            # パフォーマンス基準: 平均500ms以内、最大1秒以内
            self.assertLess(avg_time, 0.5, 
                          f"Average response time for {endpoint}: {avg_time:.3f}s > 0.5s")
            self.assertLess(max_time, 1.0,
                          f"Max response time for {endpoint}: {max_time:.3f}s > 1.0s")
        
        # 結果をログ出力
        print("\n=== Single Request Performance Results ===")
        for endpoint, stats in results.items():
            print(f"{endpoint}:")
            print(f"  Average: {stats['average']:.3f}s")
            print(f"  Max: {stats['max']:.3f}s")
            print(f"  Min: {stats['min']:.3f}s")
    
    def test_concurrent_requests_response_time(self):
        """同時リクエストのレスポンス時間テスト"""
        endpoint = '/api/v1/test/'
        concurrent_users = 10
        requests_per_user = 5
        
        def make_request():
            start_time = time.perf_counter()
            response = self.client.get(endpoint)
            end_time = time.perf_counter()
            return {
                'response_time': end_time - start_time,
                'status_code': response.status_code
            }
        
        # 同時リクエスト実行
        all_results = []
        with ThreadPoolExecutor(max_workers=concurrent_users) as executor:
            futures = []
            
            # 各ユーザーが複数回リクエスト
            for user in range(concurrent_users):
                for req in range(requests_per_user):
                    futures.append(executor.submit(make_request))
            
            # 結果を収集
            for future in as_completed(futures):
                result = future.result()
                all_results.append(result)
                # レスポンスが正常
                self.assertIn(result['status_code'], [200, 404])
        
        # パフォーマンス分析
        response_times = [r['response_time'] for r in all_results]
        avg_time = statistics.mean(response_times)
        max_time = max(response_times)
        p95_time = statistics.quantiles(response_times, n=20)[18]  # 95パーセンタイル
        
        print(f"\n=== Concurrent Request Performance Results ===")
        print(f"Users: {concurrent_users}, Requests per user: {requests_per_user}")
        print(f"Total requests: {len(all_results)}")
        print(f"Average response time: {avg_time:.3f}s")
        print(f"Max response time: {max_time:.3f}s")
        print(f"95th percentile: {p95_time:.3f}s")
        
        # パフォーマンス基準
        self.assertLess(avg_time, 1.0, f"Concurrent average time: {avg_time:.3f}s > 1.0s")
        self.assertLess(p95_time, 2.0, f"95th percentile time: {p95_time:.3f}s > 2.0s")


class MemoryUsageTest(TestCase):
    """メモリ使用量テスト"""
    
    def setUp(self):
        self.client = Client()
        self.process = psutil.Process(os.getpid())
    
    def test_memory_usage_under_load(self):
        """負荷時のメモリ使用量テスト"""
        # 初期メモリ使用量
        initial_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        
        # 大量リクエストを実行
        endpoint = '/api/v1/test/'
        request_count = 100
        
        for i in range(request_count):
            response = self.client.get(endpoint)
            self.assertIn(response.status_code, [200, 404])
            
            # 10リクエストごとにメモリをチェック
            if i % 10 == 0:
                current_memory = self.process.memory_info().rss / 1024 / 1024
                memory_increase = current_memory - initial_memory
                
                # メモリリークチェック: 100MB以下の増加を期待
                self.assertLess(memory_increase, 100,
                              f"Memory usage increased by {memory_increase:.1f}MB at request {i}")
        
        # 最終メモリ使用量
        final_memory = self.process.memory_info().rss / 1024 / 1024
        total_increase = final_memory - initial_memory
        
        print(f"\n=== Memory Usage Test Results ===")
        print(f"Initial memory: {initial_memory:.1f}MB")
        print(f"Final memory: {final_memory:.1f}MB")
        print(f"Total increase: {total_increase:.1f}MB")
        print(f"Requests processed: {request_count}")
        
        # メモリ使用量の基準
        self.assertLess(total_increase, 50,
                       f"Total memory increase: {total_increase:.1f}MB > 50MB")


class DatabasePerformanceTest(TestCase):
    """データベース操作のパフォーマンステスト"""
    
    def setUp(self):
        self.client = Client()
    
    def test_project_operations_performance(self):
        """プロジェクト操作のパフォーマンステスト"""
        operations_times = {}
        
        # プロジェクト作成テスト
        create_times = []
        for i in range(5):
            project_data = {
                "folder_name": f"perf_test_project_{i}",
                "project_name": f"パフォーマンステスト{i}",
                "description": "パフォーマンステスト用プロジェクト"
            }
            
            start_time = time.perf_counter()
            response = self.client.post('/api/v1/projects/',
                                      data=json.dumps(project_data),
                                      content_type='application/json')
            end_time = time.perf_counter()
            
            create_time = end_time - start_time
            create_times.append(create_time)
            
            # 201 Created または 409 Conflict（既存の場合）
            self.assertIn(response.status_code, [201, 409])
            
            # 作成成功時のレスポンス時間チェック
            if response.status_code == 201:
                self.assertLess(create_time, 2.0,
                              f"Project creation time: {create_time:.3f}s > 2.0s")
        
        # プロジェクト一覧取得テスト
        list_times = []
        for _ in range(10):
            start_time = time.perf_counter()
            response = self.client.get('/api/v1/projects/')
            end_time = time.perf_counter()
            
            list_time = end_time - start_time
            list_times.append(list_time)
            
            self.assertEqual(response.status_code, 200)
            self.assertLess(list_time, 0.5,
                          f"Project list time: {list_time:.3f}s > 0.5s")
        
        operations_times['create'] = {
            'average': statistics.mean(create_times),
            'max': max(create_times)
        }
        operations_times['list'] = {
            'average': statistics.mean(list_times),
            'max': max(list_times)
        }
        
        print(f"\n=== Database Operations Performance ===")
        for operation, stats in operations_times.items():
            print(f"{operation.capitalize()} operation:")
            print(f"  Average: {stats['average']:.3f}s")
            print(f"  Max: {stats['max']:.3f}s")


class ScalabilityTest(TestCase):
    """スケーラビリティテスト"""
    
    def setUp(self):
        self.client = Client()
    
    def test_increasing_load_response(self):
        """負荷増加に対するレスポンス特性テスト"""
        endpoint = '/api/v1/test/'
        load_levels = [1, 5, 10, 20]  # 同時ユーザー数
        results = {}
        
        for load in load_levels:
            def make_request():
                start_time = time.perf_counter()
                response = self.client.get(endpoint)
                end_time = time.perf_counter()
                return end_time - start_time, response.status_code
            
            # 各負荷レベルでテスト実行
            response_times = []
            with ThreadPoolExecutor(max_workers=load) as executor:
                futures = [executor.submit(make_request) for _ in range(load * 2)]
                
                for future in as_completed(futures):
                    response_time, status_code = future.result()
                    response_times.append(response_time)
                    self.assertIn(status_code, [200, 404])
            
            avg_time = statistics.mean(response_times)
            max_time = max(response_times)
            
            results[load] = {
                'average': avg_time,
                'max': max_time,
                'requests': len(response_times)
            }
            
            # スケーラビリティチェック: 負荷が増えても合理的な範囲内
            expected_max_time = 1.0 + (load - 1) * 0.1  # 負荷に応じた期待値
            self.assertLess(avg_time, expected_max_time,
                          f"Load {load}: Average time {avg_time:.3f}s > {expected_max_time:.3f}s")
        
        print(f"\n=== Scalability Test Results ===")
        for load, stats in results.items():
            print(f"Load level {load} users:")
            print(f"  Requests: {stats['requests']}")
            print(f"  Average: {stats['average']:.3f}s")
            print(f"  Max: {stats['max']:.3f}s")
            
            # 前の負荷レベルとの比較
            if load > 1:
                prev_load = load // 2 if load > 10 else load - 1
                if prev_load in results:
                    improvement_ratio = stats['average'] / results[prev_load]['average']
                    print(f"  Performance ratio vs load {prev_load}: {improvement_ratio:.2f}x")


class EndpointSpecificPerformanceTest(TestCase):
    """エンドポイント別パフォーマンステスト"""
    
    def setUp(self):
        self.client = Client()
    
    def test_file_operations_performance(self):
        """ファイル操作系エンドポイントのパフォーマンス"""
        # まずテスト用プロジェクトを作成
        project_data = {
            "folder_name": "file_perf_test",
            "project_name": "ファイルパフォーマンステスト",
            "description": "ファイル操作パフォーマンステスト"
        }
        
        response = self.client.post('/api/v1/projects/',
                                  data=json.dumps(project_data),
                                  content_type='application/json')
        
        if response.status_code not in [201, 409]:
            self.skipTest("Could not create test project")
        
        # ファイル関連エンドポイントのテスト
        file_endpoints = [
            '/api/v1/files/tree/file_perf_test/',
            '/api/v1/files/descriptions/file_perf_test/',
            '/api/v1/files/tags/file_perf_test/',
        ]
        
        for endpoint in file_endpoints:
            response_times = []
            
            for _ in range(5):
                start_time = time.perf_counter()
                
                if 'descriptions' in endpoint or 'tags' in endpoint:
                    # GET リクエスト
                    response = self.client.get(endpoint + '?file_path=test.csv')
                else:
                    # 通常のGETリクエスト
                    response = self.client.get(endpoint)
                
                end_time = time.perf_counter()
                response_times.append(end_time - start_time)
                
                # ステータスコードの確認（404も正常 - プロジェクトが存在しない場合）
                self.assertIn(response.status_code, [200, 404])
            
            avg_time = statistics.mean(response_times)
            max_time = max(response_times)
            
            print(f"\n{endpoint}:")
            print(f"  Average: {avg_time:.3f}s")
            print(f"  Max: {max_time:.3f}s")
            
            # ファイル操作は若干時間がかかる可能性があるため、基準を緩める
            self.assertLess(avg_time, 1.0,
                          f"File operation average time: {avg_time:.3f}s > 1.0s")
            self.assertLess(max_time, 2.0,
                          f"File operation max time: {max_time:.3f}s > 2.0s")