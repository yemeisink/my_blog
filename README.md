# my_blog

![1690425088877](image/README/1690425088877.png)

## Functions

1. To add posts, the title, name of the post and the content of the post will be displayed on the home page.

   ![1690425474801](image/README/1690425474801.png)
2. Display all the blog posts sorted by date (the last post is displayed first).
3. Select a certain date in the calendar and display all the posts written on this day.
4. Register in the system with the unique user name and password

   ## the bottom of the home page
5. Display the list of authors.

   ![1690425764580](image/README/1690425764580.png)
6. Show only the blog posts composed by the given author.

   ![1690425805361](image/README/1690425805361.png)

   # database schema

   ![1690426096138](image/README/1690426096138.png)

   In this module ,all the articles in the database that are displayed on the home page.

   ![1690426282738](image/README/1690426282738.png)

These users are the authors I can choose from when I post articles.

## Code

*Because this is the first html file I've ever completed*

```

{% extends 'base.html' %}
{% block content %}

    <h1> Post</h1>

    <!-- Add a button to sort posts by date -->
    <form action="{% url 'all_posts_sorted_by_date' %}" method="get">
        <button type="submit">Sort by Date</button>
    </form>

    <form action="{% url 'posts_by_date' %}" method="get">
        <label for="selected_date">Select a date:</label>
        <input type="date" id="selected_date" name="selected_date">
        <button type="submit">Search</button>
    </form>

    <ul>
    {% for post in object_list %}
        <li>
            <a href={% url 'article-detail' post.pk %}>
                {{ post.title }}
            </a>
            - {{ post.author.first_name }}
            <br />
        {{ post.body }} ''date:
        {{ post.pub_date }}''</li>
        <br />
        <br />
        <br />
        <br />
    {% endfor %}
    </ul>

    <a href="{% url 'all_authors' %}">View All Authors</a>

{% endblock %}
```

1. I can do what I want to do with the button.
2. I can click on the text to jump to the web page
