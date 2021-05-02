---
layout: main
title: Tags
---

{% include header.html %}

Par tag : <span id="tag-name"></span>

<div id="comics-list">
{% assign comics = site.data.database.comics | where_exp: "item", "item.hide != true" | sort_natural: "name" %}
{% include comics_list.html %}
</div>

<script type="text/javascript">

    // case insensitive "contains" selector
    // https://stackoverflow.com/questions/8746882/jquery-contains-selector-uppercase-and-lower-case-issue
    jQuery.expr[':'].icontains = function(a, i, m) {
        return jQuery(a).text().toUpperCase()
            .indexOf(m[3].toUpperCase()) >= 0;
    };

    var getUrlParameter = function getUrlParameter(sParam) {
        var sPageURL = window.location.search.substring(1),
            sURLVariables = sPageURL.split('&'),
            sParameterName,
            i;

        for (i = 0; i < sURLVariables.length; i++) {
            sParameterName = sURLVariables[i].split('=');

            if (sParameterName[0] === sParam) {
                return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
            }
        }
    };
    $(document).ready(() => {

        var tag = getUrlParameter('t');
        if(!tag) return;

        $('#comics-list .comics-list-item').hide();


        $('#tag-name').html(decodeURIComponent(tag).replace(/-/g, ' '));

        var $nodes = $('#comics-list').find('.comic-tag[data-tag="' + tag + '"]').closest('.comics-list-item');
        var $nodes2 = $('#comics-list').find('.comic-title:icontains("' + tag + '")').closest('.comics-list-item');
        
        $nodes = $nodes.add($nodes2);
        
        $nodes.show();

        $('.comics-count').html($nodes.length);
    });
</script>