import requests
def fetch_comments_from_api(post_id):
    url = f"https://jsonplaceholder.typicode.com/comments?postId={post_id}"
    
    try:

        response = requests.get(url)
        if response.status_code == 200:
            comments = response.json()  
            return comments
        else:
            print(f"Không thể lấy dữ liệu từ API. Mã lỗi: {response.status_code}")
            return None
    except Exception as e:
        print(f"Đã xảy ra lỗi khi kết nối API: {e}")
        return None
def display_comments(comments):
    if comments is None:
        return
    print("Danh sách các bình luận nổi bật (giới hạn 3 bài đầu):")
    for comment in comments[:3]:  
        print(f"Post ID: {comment['postId']}, ID: {comment['id']}")
        print(f"Name: {comment['name']}")
        print(f"Email: {comment['email']}")
        print(f"Body: {comment['body']}")
        print('-' * 40)
def main():
    post_id = 1 
    comments = fetch_comments_from_api(post_id)  
    display_comments(comments)                   
    
if __name__ == "__main__":
    main()
