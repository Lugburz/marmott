
// menu builder
Vue.component('mymenu', {
    // template: '#template-menu',
    data: function() { 
        return {
            menuItems: [
                { name : "Liste complète", link : "" },
                // { name : "Tags", link : "tags" },
                // { name : "Prêts", link : "lended" },
            ]
        }
    },
});


var app = new Vue(
    {
        el: "#app",
        data: {

        },
        methods: {
            onAddFilter: function (dunno) {
                console.log("hello from app", dunno);
            }
        }
    }
);
