<template>
    <RouterLink 
        :to="{ name: 'question-editor', params: { slug: slug} }"
        class="btn btn-sm btn-warning">
        Modifica                
    </RouterLink>
    <button class="btn btn-sm btn-danger mx-1" @click="showDeleteConfirmBtn = !showDeleteConfirmBtn">Elimina</button>
    <button v-show="showDeleteConfirmBtn" class="btn btn-outline-danger btn-sm" @click="deleteQuestion">Conferma</button>
</template>

<script>
import { RouterLink, RouterView } from 'vue-router';
import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";

export default {
    name: "QuestionAction",
    props: {
        slug: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            showDeleteConfirmBtn: false
        }
    },
    methods: {
        async deleteQuestion() {
            const endpoint = `${endpoints["questionsCRUD"]}${this.slug}/`;
            try {
                await axios.delete(endpoint);
                this.$router.push(
                    {
                        name: "home"
                    }
                )
            } catch (error) {
                console.log(error);
                alert(error.response.statusText);
            }
        }
    }
}
</script>