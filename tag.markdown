---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: main
---

{% include header.html %}

Par tag : <span id="tag-name"></span>

<div id="comics-list">
{% assign comics = site.data.database.comics | sort: "name" %}
{% include comics_list.html %}
</div>

<script type="text/javascript">
    
    $(document).ready(() => {

        var tag = window.location.href.match(/tag\/(.*)$/);
        if(!tag || tag.length < 2) return;
        tag = tag[1];

        $('#tag-name').html(decodeURIComponent(tag).replace(/-/g, ' '));

        $('#comics-list .comics-list-item').hide();
        $('#comics-list').find('.comic-tag[data-tag="' + tag + '"]').closest('.comics-list-item').show();
    });
</script>