import requests
def fetch_posts_from_api():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            posts = response.json() 
            return posts
        else:
            print(f"Không thể lấy dữ liệu từ API. Mã lỗi: {response.status_code}")
            return None
    except Exception as e:
        print(f"Đã xảy ra lỗi khi kết nối API: {e}")
        return None
def display_posts(posts):
    if posts is None:
        return
    
    print(f"Tổng số bài post: {len(posts)}")

    for post in posts:
        print(f"UserID: {post['userId']}, ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print('-' * 40)
def main():
    posts = fetch_posts_from_api()  
    display_posts(posts)            
    
if __name__ == "__main__":
    main()
