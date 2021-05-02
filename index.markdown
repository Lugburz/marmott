---
layout: main
title: Index
---
{% include header.html %}
{% assign allcomics = site.data.database.comics | where_exp: "item", "item.hide != true" %}
{% assign comics = allcomics | sort_natural: "name" %}

<div id="comics-list">
{% include comics_list.html %}
</div>