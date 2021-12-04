// comic list
Vue.component('comics-list', {
    data: function() {
        let converter = new showdown.Converter();
        let tags = ['BD', 'manga', 'comics'].concat( database["comics"].reduce((acc, comic) => { acc.push(...comic.tags); return acc; }, [])
            .filter((v, i, a) => a.indexOf(v) === i).filter((tag) => { return tag != "BD" && tag != "manga" && tag != "comics"} ).sort());
        let content = database["comics"]
            .filter(comic => !comic.hide)
            .map((comic) => {
                let c = comic;
                if(c.mkdw)
                    c.description = converter.makeHtml( Tools.loadFile(c.mkdw) );

                comic.tags.push( ...comic.author.split(' & ') );

                return c;
            }).sort((a, b) => { return a.name.toUpperCase() > b.name.toUpperCase() })

        return {
            filters : [],
            comics: content,
            tags: tags
        }
    },
    computed: {
        filteredComics : function() {
            return this.comics.filter((comic) => {
                let match = 1;
                this.filters.forEach((f) => {
                    match = match && comic.tags.indexOf(f) > -1;
                });
                return match;
            } );
        }
    },
    methods: {
        onAddFilter: function (tag, replace_all) {
            if(replace_all) {
                this.filters = [ tag ];
                return;
            }
            if(this.filters.indexOf(tag) == -1)
                this.filters.push(tag);
        },
        onRemoveFilter: function (tag, replace_all) {
            let index = this.filters.indexOf(tag);
            if(index > -1)
                this.filters.splice(index, 1);
        },
        onRemoveAllFilters: function (tag) {
            this.filters = [];
        },     

    }
});