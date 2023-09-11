<template>
    <div class="mt-3">
        <p class="mb-1">
            <strong>{{ answer.author }}</strong>, {{ answer.created_at }}
        </p>
        <div>
            <textarea v-if="editingAnswer" v-model="answer.body" class="form-control" rows="5"></textarea>
            <p v-else>{{ answer.body }}</p>
            <p v-if="error">{{ error }}</p> 
        </div>
        <div v-if="isAnswerAuthor">
            <button v-if="editingAnswer" @click="updateAnswer" class="btn btn-sm btn-warning">Aggiorna</button>
            <button v-else @click="editingAnswer = true" class="btn btn-sm btn-warning">Aggiorna</button>
            <button class="btn btn-sm btn-danger mx-1" @click="showDeleteConfirmBtn = !showDeleteConfirmBtn">Elimina</button>
            <button v-show="showDeleteConfirmBtn" class="btn btn-outline-danger btn-sm" @click="TriggerDeleteAnswer">Conferma</button>
        </div>  
        <div v-else>
            <button class="btn btn-sm" 
            :class="{'btn-warning': userLikedAnswered, 'btn-outline-danger': !userLikedAnswered}" 
            @click="toggleLike">
                Mi piace
                <span>{{ likesCounter }}</span>
            </button>
             
            
        </div>
        <hr>
    </div>
</template>

<script>
import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";
export default {
    name: 'AnswerComponent',
    props: {
        answer: {
            type: Object,
            required: true
        },
        requestUser: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            editingAnswer: false,
            error: null,
            showDeleteConfirmBtn: false,
            userLikedAnswered: this.answer.user_has_liked_answered,
            likesCounter: this.answer.likes_count
        }
    },
    computed: {
        isAnswerAuthor() {
            return this.answer.author === this.requestUser;
        }
    },
    methods: {
        async updateAnswer() {
            if (!this.answer.body) {
                this.error = "Non puoi codividere una risposta vuota";
                return;
            }
            const endpoint = `${endpoints["AnswerDetail"]}${this.answer.uuid}/`;
            try {
                await axios.put(endpoint, { body: this.answer.body });
                this.editingAnswer = false;
                if ( this.error) {
                    this.error = null;
                }  
            } catch (error) {
                console.log(error.response);
                this.error = error.response.statusText;          
            }
        },
        TriggerDeleteAnswer() {
            this.$emit("delete-answer", this.answer);

        },
        toggleLike() {
            this.userLikedAnswered ? this.unLikeAnswer(): this.likeAnswer();
        },
        async likeAnswer() {
            this.userLikedAnswered = true;
            this.likesCounter += 1;
            const endpoint = `${endpoints["AnswerLike"]}${this.answer.uuid}/`;
            try {
                await axios.post(endpoint);
            } catch (error) {
                console.log(error.response);
                this.error = error.response.statusText;                 
            }
        },
        async unLikeAnswer() {
            this.userLikedAnswered = false;
            this.likesCounter -= 1;
            const endpoint = `${endpoints["AnswerLike"]}${this.answer.uuid}/`;
            try {
                await axios.delete(endpoint);
            } catch (error) {
                console.log(error.response);
                this.error = error.response.statusText;                 
            }
        },
    }
    
}
</script>