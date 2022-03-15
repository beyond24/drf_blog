import {createWebHistory, createRouter} from "vue-router";
import HomePage from "@/views/HomePage";
import ArticleDetail from "@/views/ArticleDetail";
import LoginPage from "@/views/LoginPage";

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
    {
        path:"/login",
        name:"LoginPage",
        component:LoginPage,
    },
];

const router = createRouter({
    history:createWebHistory(),
    routes,
});

export default router;