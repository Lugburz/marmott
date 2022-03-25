<template>
    <div class="comic-text collapsed">
        <div v-html="content"></div>
        <div class="collasped-gradient" ></div>
        <span v-on:click="handleExpand" class="see-more">
            Voir plus
        </span>
    </div>
</template>

<script>
    export default {
        name: 'ComicsDescription',
        mounted() {
            if(this.$el.offsetHeight < 220) {
                this.$el.getElementsByClassName('see-more')[0].remove();
                this.$el.classList.remove("collapsed");
                this.$el.getElementsByClassName('collasped-gradient')[0].remove();
            }
        },
        props : {
            content : String
            },
        methods : {
            handleExpand: function() {
                this.$el.getElementsByClassName('collasped-gradient')[0].remove();
                this.$el.classList.remove("collapsed");
                this.$el.getElementsByClassName('see-more')[0].remove();

            }
        }
    }
</script>

<style scoped>

    span {
        cursor: pointer;
        z-index: 11;
        display: block;
        position: absolute;
        margin-top: 20px;
        bottom: 0;
    }

    .collapsed {
        max-height: 200px;
        overflow-y: hidden;
        position: relative;
    }

    .collasped-gradient {
        background: rgb(255,255,255);
        background: linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(255,255,255,1) 65%, rgba(255,255,255,1) 100%);
        position: absolute;
        height: 100%;
        width: 100%;
        z-index: 10;
        left:0;
        /* top:0; */
        bottom: -60px;
    }
</style>