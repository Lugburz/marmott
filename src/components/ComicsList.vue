<template>
    <div id="comics-list" style="margin-top: 50px;">
        <div name="filter-tags" style="position: fixed;width:100%;background-color: white;border: 1px solid gray;min-height: 20px;top:0;left:0;">
            <span>Filtres : </span>
            <input v-on:change="onCustomFilter" v-model="customFilter" type="text" >

            <span class="comic-tag">
                <a v-on:click="onRemoveAllFilters">X</a>
            </span>
            
            <span v-for="tag in filters" class="comic-tag" v-bind:key="tag">
                <a v-html="tag" v-on:click="onRemoveFilter(tag)"></a>
            </span>
        </div>
        <div style="margin-top: 10px;" name="all-tags">
            <span v-for="tag in tags" class="comic-tag" v-bind:key="tag">
                <a v-html="tag" v-on:click="onAddFilter(tag)"></a>
            </span>
        </div>
        <div>{{ filteredComics.length }} / {{ comics.length }} BDs</div>
        <div v-for="comic in filteredComics" class="comics-list-item" v-bind:key="comic">
            <div class="comic-thumbnail">
                <a v-bind:href="'./img/comics/' + comic.image">
                    <img v-bind:src="'./img/comics/thumbnails/' + comic.image" v-bind:alt='comic.name' />
                </a>
            </div>
            <ComicsDescription @add-comic-tag="onAddFilter" v-bind:comic="comic" />
        </div>
    </div>
</template>

<script>
// include whole database.json as a variable
import database from "../assets/database.json"
import ComicsDescription from "./ComicsDescription.vue"

export default {
    components : {
        ComicsDescription
    },
    name: 'ComicsList',
    data: function() {
        // force comics type first
        let tags = ['BD', 'manga', 'comics'];
        
        // get appearences for all tags
        let tags_appearences = database["comics"].reduce((acc, comic) => {
            comic.tags.forEach(tag => {
                if(tag == "BD" || tag == "manga" || tag == "comics") return;
                if(!acc[tag])
                    acc[tag] = 0
                acc[tag] += 1;
            });
            return acc;
        }, {});

        // only keep tags appearing at least twice
        tags = tags.concat(
            Object.keys(tags_appearences).filter(tag => tags_appearences[tag] > 1 ).sort()
        );

        // add authors as comics tags (not global tags though) 
        let content = database["comics"]
            .filter(comic => !comic.hide)
            .map((comic) => {
                comic.tags.push( ...comic.author.split(' & ') );
                return comic;
            }).sort((a, b) => { return a.name.toUpperCase() > b.name.toUpperCase() })

        return {
            filters : [],
            comics: content,
            tags: tags,
            customFilter : ""
        }
    },
    computed: {
        filteredComics : function() {
            const queryString = window.location.search;
            // remove search, add it as tag
            if(queryString) {
                const urlParams = new URLSearchParams(queryString);
                let additional_tags = urlParams.get('tag');

                var other_tags = additional_tags ? additional_tags.split(',') :  [];
                other_tags.forEach(tag => this.onAddFilter(tag) );
            }
            return this.comics.filter((comic) => {
                let match = 1;
                this.filters.forEach((f) => {
                    if(f.startsWith("Custom: ")) {
                        let ctag = f.replace("Custom: ", "").toLowerCase();
                        let intags = comic.tags.filter(tag => tag.toLowerCase().indexOf(ctag) > -1).length > 0;
                        let intitle = comic.name.toLowerCase().indexOf(ctag) > -1;
                        match = match && (intags || intitle);
                    } else {
                        let intags = comic.tags.indexOf(f) > -1; 
                        match = match && intags;
                    }
                    // to return false and exit early if we already matched 
                    return !match;
                });
                return match;
            } );
        }
    },
    methods: {
        updateTagsInURL: function() {
            let newtagstring = this.filters.join(',');
            var url = new URL( window.location.href );
            url.searchParams.set('tag', newtagstring);
            window.history.pushState({}, document.title, url.href);
        },
        onAddFilter: function (tag, replace_all) {
            if(replace_all) {
                this.filters = [];
            }
            if(this.filters.indexOf(tag) == -1) 
                this.filters.push(tag);
            this.updateTagsInURL();
        },
        onRemoveFilter: function (tag) {
            let index = this.filters.indexOf(tag);
            if(index > -1)
                this.filters.splice(index, 1);
            this.updateTagsInURL();
        },
        onRemoveAllFilters: function () {
            this.filters = [];
            this.updateTagsInURL();
        },
        onCustomFilter: function () {
            // remove all custom filters first
            this.filters = this.filters.filter(f => !f.startsWith("Custom: "));
            this.filters.push("Custom: " + this.customFilter);
            this.customFilter = "";
            this.updateTagsInURL();
        },
    }
}
</script>