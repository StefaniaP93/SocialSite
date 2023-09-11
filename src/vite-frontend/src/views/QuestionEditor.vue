<template>
    <div class="container mt-2">
        <h1>Fai una domanda</h1>
        <form @submit.prevent="onSubmit">
            <textarea v-model="questionBody" class="form-control" rows="5"></textarea>
            <button type="submit" class="btn btn-pink mt-3">Pubblica Domanda</button>
        </form>
        
    </div>

</template>

<script>
import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";

export default {
    name: "QuestionEditor",
    props: {
        slug: {
            type: String,
            required: false
        }
    },
    data() {
        return {
            questionBody: null,
            error: null,
        }        
    },
    methods: {
        async performNetworkRequest() {
            let endpoint = endpoints ["questionsCRUD"];
            let method = "POST";
            if (this.slug !== undefined && this.slug !== "") {
                endpoint += `${this.slug}/`
                method = 'PUT';
            }
            const data = { content: this.questionBody }
            try {
                const response = await axios({
                    method: method,
                    url: endpoint,
                    data: data
                })
                
                this.$router.push(
                    {
                        name: "question-view",
                        params: { slug: response.data.slug }
                    }
                    );
            } catch (error) {
                alert(error.response.statusText);
            }
        },
        onSubmit() {
            if (!this.questionBody) {
                this.error = "Non puoi condividere una domanda vuota!";
            }else if (this.questionBody.length > 240) {
                this.error = "La domanda non può contenere più di 240 caratteri";
            }else {
                this.performNetworkRequest();
            }
            
        }
    },
    async beforeRouteEnter(to, from, next) {
            if (to.params.slug !== undefined && to.params.slug !== "") {
                const endpoint = `${endpoints["questionsCRUD"]}${to.params.slug}/`;
                try {
                    const response = await axios.get(endpoint);
                    return next(vm => vm.questionBody = response.data.content);
                } catch (error) {
                    console.log(error.response);
                    alert(error.response.statusText);
                }
            } else {
                return next();
            }
        },
        created() {
            document.title = "Editor - QuestionTime"       
        }
};

</script>

<style>
.btn-pink {
  background-color: #c765e5d5;
  color: white;
  
}
</style>