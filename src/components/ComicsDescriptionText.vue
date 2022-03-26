<template>
    <div class="comic-text collapsed">
        <div class="content" v-html="content"></div>
        <span v-on:click="handleExpand" class="see-more">
            Voir plus
        </span>
    </div>
</template>

<script>
    export default {
        name: 'ComicsDescriptionText',
        mounted() {
            var content = this.$el.getElementsByClassName("content")[0];
            var height_set = false;

            for (let i = 0; i < content.children.length; i++) {
                let child = content.children[i];
                if(child.offsetTop > 200) {
                    if(i > 1)
                        child = content.children[i - 1];
                    content.style.height = child.offsetTop + "px";
                    height_set = true;
                    break;
                }
            }

            if(!height_set)
                this.handleExpand();
        },
        props : {
            content : String
        },
        methods : {
            handleExpand: function() {
                var content = this.$el.getElementsByClassName("content")[0];
                content.style.height = null;
                this.$el.classList.remove("collapsed");
                this.$el.getElementsByClassName('see-more')[0].remove();
            }
        }
    }
</script>

<style scoped>

    .comic-text {
        padding: 4px;
    }

    .see-more {
        cursor: pointer;
        font-style: oblique;
        font-weight: bold;
        font-size: 1.2em;
        text-decoration: underline;
        margin-top: 3px;
    }

    .collapsed {
        position: relative;
    }

    .content {
        line-height: 20px;
    }

    .collapsed .content {
        overflow:hidden;
    }
</style>