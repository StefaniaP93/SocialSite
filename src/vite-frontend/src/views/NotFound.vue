<template>
    <div class="container mt-3"  >
        <h1 class="text-center">{{ message }}</h1>
    </div>
</template>

<script>
export default{
    name: "NotFound",
    data() {
        return {
            message: "Pagina non trovata"
        }
    },
    created() {
        document.title = this.message
    }
}

</script>