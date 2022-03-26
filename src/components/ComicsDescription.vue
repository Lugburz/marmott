<template>
    <div class="comic-description">
        <span class="comic-title">{{ comic.name }}
            <template v-if="comic.owned">
                <template v-if="comic.rented_by">
                    <span class="comic-rented" title="Emprunté"></span>
                    <span class="comic-rented-by">(emprunté par {{comic.rented_by}})</span>
                </template>
                <template v-else>
                    <span class="comic-available" title="Disponible"></span>
                </template>
            </template>
            <template v-else>
                <span class="comic-unavailable" title="Indisponible"></span> 
            </template>
        </span>
        <span class="comic-author">{{ comic.author }}</span>
        <span  v-if="comic.volumes" class="comic-volumes">
            {{ comic.volumes }}
            <template v-if="comic.volumes == 1">
                volume
            </template>
            <template v-else>
                volumes
            </template>
            <template v-if="comic.still_going">
                (série en cours)
            </template>
        </span>
        <ComicsDescriptionText v-bind:content="comic.description" />
        <div class="comic-tags">
            <span v-for="tag in comic.tags" class="comic-tag" data-tag="tag" v-bind:key="tag">
                <a v-html="tag" @click="buttonClickHandler(tag)" ></a>
            </span>
        </div>
    </div>
</template>

<script>

    import ComicsDescriptionText from "./ComicsDescriptionText.vue";
    export default {
        components : {
            ComicsDescriptionText
        },
        name: 'ComicsDescription',
        props : {
            comic : Object
        },
        methods: {
            buttonClickHandler(tag) {
                this.$emit('add-comic-tag', tag, true)
            }
        }
    }
</script>
