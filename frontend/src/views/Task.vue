<template>
  <v-main>
    <h1 class="ml-16">Напишите метод, суммирующий два числа a и b.</h1>
    <p
        v-if="errorMessage"
    >{{ errorMessage }}</p>
    <v-container
        fluid
        :class="containerStatus"
    >
      <v-row
          justify="center"
          align="center"
      >
        <v-col
            cols="6"
            md="6"
        >
          <v-progress-circular
              indeterminate
              color="primary"
              v-if="loader"
              :size="50"
          ></v-progress-circular>
          <codemirror
              v-model="code"
              :options="cmOptions"
              v-else
          ></codemirror>

        </v-col>
      </v-row>
      <p class="font-weight-bold ml-2"
         v-if="status !== 'evaluation'"
      >
        {{ textMessages[status] }}
      </p>
      <v-row
          v-if="!status || status === 'unevaluated'">
        <v-col
            md="2"
        >
          <v-btn
              color="primary"
              @click="checkCode"
          >
            Отправить
          </v-btn>
        </v-col>
      </v-row>
      <v-row
          v-if="status==='correct'"
      >
        <v-col
            md="2"
        >
          <v-btn
              color="primary"
          >
            Следующий шаг
          </v-btn>
        </v-col>
        <v-col
            md="2"
        >
          <v-btn
              color="primary"
              @click="checkCode"
          >
            Решить заново
          </v-btn>
        </v-col>
      </v-row>
      <v-row
          v-if="status==='wrong'"
      >
        <v-col
            md="2"
        >
          <v-btn
              color="primary"
              @click="checkCode"
          >
            Отправить
          </v-btn>
        </v-col>
        <v-col
            md="2"
        >
          <!-- it's obvious here should be different logic -->
          <v-btn
              color="primary"
              @click="checkCode"
          >
            Начать сначала
          </v-btn>
        </v-col>

      </v-row>
    </v-container>
  </v-main>
</template>

<script>

import {codemirror} from "vue-codemirror/src";
import 'codemirror/mode/python/python.js'

import 'codemirror/theme/elegant.css'
import {stepikApi} from "@/services/api";

export default {
  name: 'Task',
  data: () => ({
    textMessages: {
      "unevaluated": "К сожалению, не удалось проверить Ваше решение. Попробуйте еще раз.",
      "correct": "Ура, все верно!",
      "wrong": "К сожалению, пока что неверно. Попробуйте еще раз!"
    },
    code: null,
    cmOptions: {
      tabSize: 4,
      mode: 'python',
      theme: 'elegant',
      lineNumbers: true,
      line: true,
    },
    polling: null,
    status: null,
    errorMessage: null,
  }),
  computed: {
    loader: function () {
      return this.status === "evaluation"
    },
    containerStatus: function () {
      if (this.status === "wrong") {
        return "red lighten-5"
      } else if (this.status === "correct") {
        return "green lighten-5"
      } else if (this.status === "unevaluated") {
        return "white lighten-5"
      } else {
        return "grey lighten-5"
      }
    },
  },
  async created() {
    const lastSolution = await this.getLastSolution()

    if (Object.keys(lastSolution).length === 0) {
      return
    }
    this.code = lastSolution.code
    this.status = lastSolution.status

  }
  ,
  methods: {
    async checkCode() {

      const codeObject = {"code": this.code}

      const response = await stepikApi.checkCode(codeObject)
      if (response.error) {
        this.errorMessage = response.error
        return
      } else {
        this.errorMessage = null
      }
      const solutionId = response.solution_id
      this.status = response.status

      this.polling = setInterval(async () => {
        await this.processSolutionStatus(solutionId);
      }, 1000);

    }
    ,

    async getLastSolution() {
      return await stepikApi.retrieveLastSolution()
    }
    ,

    async processSolutionStatus(id) {
      const response = await stepikApi.checkSolutionStatus(id)

      this.status = response.status

      if (response.status !== "evaluation") {
        clearInterval(this.polling)
      }
    }
  }
  ,
  components: {
    codemirror
  }

}
</script>
