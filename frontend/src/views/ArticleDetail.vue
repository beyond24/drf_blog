<template>

    <BlogHeader/>

    <!--  暂时留空  -->

    <BlogFooter/>

</template>

<script>
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'

    export default {
        name: 'ArticleDetail',
        components: {BlogHeader, BlogFooter}
    }
</script>