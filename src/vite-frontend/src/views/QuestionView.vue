<template>
    <div class="container" v-if="question" >
        <h1>{{ question.content }}</h1>
        <p class="mb-0">
            Pubblicata da: 
            <span class="question-author">{{ question.author }}</span>
        </p>
        <p class="mb-1">{{ question.created_at }}</p>
        <div v-if="isQuestionAuthor" class="mb-3">
            <QuestionAction :slug="question.slug" />
        </div>
        <div v-if="userHasAnswered">
            <p>Hai Risposto a questa domanda!</p>
        </div>
        <div v-else-if="showForm">
            <p>Rispondi alla domanda!</p>
            <form @submit.prevent="onSubmit">
                <textarea v-model="newAnswerBody" class="form-control" rows="5"></textarea>
                <button type="submit" class="btn btn-sm btn-outline-success mt-1">Rispondi</button>
            </form> 
        <p v-if="error">{{ error }}</p>       
        </div>
        <div v-else>
            <button class="btn btn-sm btn-success mt-1" @click="showForm=true">Rispondi alla domanda</button>
        </div>
        
        <div>
            <AnswerComponent v-for="answer in answers" 
            :answer="answer" 
            :requestUser="requestUser" 
            :key="answer.uuid" 
            @delete-answer="deleteAnswer"/>

            <p v-show="loadingAnswer">... caricamento ...</p>
            <button v-show="next" class="btn btn-sm btn-outline-success" @click="getQuestionAnswers">Carica altre Risposte</button>
        </div>

    </div>
    <div v-else>
        <h1 class="text-danger text-center">Domanda non trovata!</h1>
    </div>
    
    
</template>

<script>
import { RouterLink, RouterView } from 'vue-router';
import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";
import AnswerComponent from '../components/AnswerComponent.vue';
import QuestionAction from '../components/QuestionAction.vue';

export default {
  name: "QuestionView",
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
    components: {
        AnswerComponent,
        QuestionAction
    },
    data() {
        return {
            question: {},
            answers: [],
            next: null,
            loadingAnswer: false, 
            requestUser: null,
            userHasAnswered : false,
            showForm: false,
            newAnswerBody: null,
            error: null
        };
    },
    computed: {
        isQuestionAuthor() {
            return this.question.author === this.requestUser;
        }
    },
    methods: {
        setPageTitle(title) {
            document.title = title;
        },    
        setRequestUser() {
            this.requestUser = window.localStorage.getItem("username");
        },
        async getQuestionsData() {
        const endpoint = `${endpoints['questionsCRUD']}${this.slug}/`;
        try {
            const response = await axios.get(endpoint);
            this.question = response.data;           
            this.userHasAnswered = response.data.user_has_answered;
            this.setPageTitle(response.data.content);      
        } catch (error) {
            console.log(error);
            this.question = null;
            this.setPageTitle(error.response.statusText);
        }
        },
        async getQuestionAnswers() {
            let endpoint = `${endpoints['questionsAnswersList']}${this.slug}/`;
            if (this.next) {
                endpoint = this.next;
            }
            this.loadingAnswer = true;
            try {
                const response = await axios.get(endpoint);
                this.answers.push(...response.data.results);
                this.loadingAnswer = false;
                if (response.data.next) {
                    this.next = response.data.next;
                } else {
                    this.next = null;
                }
            
            } catch (error) {
                console.log(error);
                alert(error.response.statusText);
            }
        },
        async onSubmit() {
            if (!this.newAnswerBody) {
                this.error = "Non puoi pubblicare una risposta vuota!";
                return;
            } 
            const endpoint = `${endpoints["questionsNewAnswer"]}${this.slug}/`;
            try {
                const response = await axios.post(endpoint, {body: this.newAnswerBody});                
                this.answers.unshift(response.data); 
                this.newAnswerBody = null;
                this.showForm = false;
                this.userHasAnswered = true;
                if ( this.error) {
                    this.error = null;
                }                
            } catch (error) {
                console.log(error);
                this.error = response.error.statusText;
            }
        },
        async deleteAnswer(answer) {            
            const endpoint = `${endpoints["AnswerDetail"]}${answer.uuid}/`;
            try {
                await axios.delete(endpoint);
                this.answers.splice(this.answers.indexOf(answer), 1);
                this.userHasAnswered = false;
            } catch (error) {
                console.log(error);
                this.error = response.error.statusText;               
            }
        }
    },
    created() {
        this.getQuestionsData(); 
        this.getQuestionAnswers();
        this.setRequestUser();
    },
    
};
</script>

<style scoped>
.question-author {
  font-weight: bold;
  color: #b01db0;
}
</style>