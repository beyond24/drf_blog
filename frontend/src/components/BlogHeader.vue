<template>
    <div id="header">
        <div class="grid">
            <div></div>
            <h1>My Drf-Vue Blog</h1>
            <SearchButton/>
        </div>

        <hr>
    </div>
</template>

<script>
import SearchButton from "@/components/SearchButton";
export default {
    name: "BlogHeader",
    components:{SearchButton},
    data: function () {
            return {
                username: '',
                hasLogin: false,
                // searchText 变量删除
            }
        },


}
</script>

<style scoped>
#header {
    text-align: center;
    margin-top: 20px;
}

.grid {
    display: grid;
    grid-template-columns: 1fr 4fr 1fr;
}


</style>