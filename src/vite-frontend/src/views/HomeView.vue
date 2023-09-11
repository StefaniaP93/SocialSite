<template>
  <main>
    <div class="container">
      <div v-for="question in questions" :key="question.uuid">
        <div class="card p-2 mb-4 shadow rounded">
          <div class="card-body">
            <p class="mb-0">
              Pubblicata da: 
              <span class="question-author">{{ question.author }}</span>
            </p> 
            <h2>
              <RouterLink :to="{ name: 'question-view', params: { slug: question.slug }}" class="question-link">
                {{ question.content }}
              </RouterLink>
            </h2>
            <p class="mb-0">Risposte: {{ question.answers_count }}</p>
          </div>
        </div>
      </div>
      <div class="my-4">
        <button class="btn btn-sm btn-success" v-show="next" @click="getQuestions">Carica ancora</button>
      </div>
    </div>
  </main>

</template>

<script>
import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";

export default {
  name: "HomeView",
  data() {
    return {
      questions: [],
      next: null,
    }
  },
  methods: {
    async getQuestions() {
      let endpoint = endpoints["questionsCRUD"];
      if (this.next) {
        endpoint = this.next;
      }
      try {
        const response = await axios.get(endpoint);
        this.questions.push(...response.data.results);
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
  },
  created() {
    document.title = "QuestionTime";
    this.getQuestions();
  },
};
</script>

<style scoped>
.question-author {
  font-weight: bold;
  color: #b01db0;
}

.question-link {
  font-weight: 600;
  color: black;
  text-decoration: none;
}

.question-link:hover {
  color: #587694;
}
</style>