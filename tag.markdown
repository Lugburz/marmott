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

        $('#tag-name').html(decodeURIComponent(tag).replace(/-/g, ' '));

        $('#comics-list .comics-list-item').hide();
        $('#comics-list').find('.comic-tag[data-tag="' + tag + '"]').closest('.comics-list-item').show();
    });
</script>