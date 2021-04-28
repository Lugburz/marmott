---
layout: main
title: Par auteur
---

{% include header.html %}
{% assign allcomics = site.data.database.comics | where_exp: "item", "item.hide != true" %}
{% assign comics = allcomics | sort: "author" %}

Par auteur.

<div id="comics-list">
{% assign comics = site.data.database.comics | where_exp: "item", "item.hide != true" |  sort: "author" %}
{% include comics_list.html %}
</div>