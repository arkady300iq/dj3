import django_setup
from datetime import datetime

from myapp.models import Post, Comments

def add_post(name, description, date):
    post = Post(
        name = name,
        description = description,
        date = date
    )
    post.save()

    return post


def add_comments_to_post(post_id, author, text, date_create):
    post = Post.objects.get(id=post_id)
    comment = Comments(
        post = post,
        author = author,
        text = text,
        date_create = date_create
    )
    comment.save()

    return comment

def edit_post_description(post_id, new_description):
    post = Post.objects.get(id=post_id)  
    post.description = new_description
    post.save()
    return post


def main():
    while True:
        question = int(input("If u want to add new post, type 1:\nIf u want add new comment to post, type 2:\nIf to edit post description, type 3:\nIf u want exit , type 4:"))

        match question:
            case 1:
                name_post = input("Enter new post name: ")
                description_post = input("Enter new post description: ")
                date_input = input("Enter new post date (YYYY-MM-DD): ")
                date_post = datetime.strptime(date_input, '%Y-%m-%d')
                print(add_post(name_post, description_post, date_post))
                print(f"Post {name_post} successfully added")

        match question:
            case 2:
                post_id = int(input("Enter post id to comment on: "))
                author = input("Enter author name: ")
                text = input("Enter your comment:")
                date_create_input =  input("Enter new comment date (YYYY-MM-DD): ")
                date_create = (datetime.strptime(date_create_input, '%Y-%m-%d'))
                print(add_comments_to_post(post_id, author, text, date_create))
                print(f"Comment {post_id} successfully added")

        match question:
            case 3:
                post_id = int(input("Enter post id to edit"))
                new_description = input("Enter new description")
                print(edit_post_description(post_id, new_description))
                print(f"Description {post_id} successfully edited")

        match question:
            case 4:
                break


if __name__ == "__main__":
    main()
                


'''not_need = Post.objects.get(id=6)
not_need.delete()
'''