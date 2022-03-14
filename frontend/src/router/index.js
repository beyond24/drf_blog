import {createWebHistory, createRouter} from "vue-router";
import HomePage from "@/views/HomePage";
import ArticleDetail from "@/views/ArticleDetail";

const routes = [
    {
        path:"/",
        name:"HomePage",
        component:HomePage,
    },
    {
        path:"/article/:id",
        name:"ArticleDetail",
        component:ArticleDetail,
    },
];

const router = createRouter({
    history:createWebHistory(),
    routes,
});

export default router;