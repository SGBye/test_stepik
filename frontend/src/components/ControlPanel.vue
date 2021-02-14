<template>
  <v-col cols="3">
    <v-sheet rounded="lg">
      <v-list color="transparent">
        <v-list-item
            v-for="task in tasks"
            :key="task.id"
            link
        >
          <v-list-item-content>
            <v-list-item-title>
              {{ task.verbose_name }}
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-divider class="my-2"></v-divider>

        <v-list-item
            link
            color="grey lighten-4"
            @click="ping"
        >
          <v-list-item-content>
            <v-list-item-title>
              Refresh
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-sheet>
  </v-col>
</template>

<script>
import {stepikApi} from "@/services/api";

export default {
  name: "ControlPanel",
  data: () => ({
    tasks: [{"verbose_name": "Сумма", "id": 'summ'}],
  }),
  async mounted() {
  },
  methods: {
    async ping() {
      await stepikApi.ping()
    }
  }
}
</script>

<style scoped>

</style>
