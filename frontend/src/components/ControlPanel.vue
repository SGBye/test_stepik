<template>
    <v-col cols="3">
        <v-sheet rounded="lg">
            <v-list color="transparent">
                <v-list-item
                    v-for="classifier in classifiers"
                    :key="classifier.id"
                    replace
                    :to="{ name: 'settingsList', params: { classifier: classifier.id }}"
                >
                    <v-list-item-content>
                        <v-list-item-title>
                            {{ classifier.verbose_name }}
                        </v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-sheet>
    </v-col>
</template>

<script>
import {scorickApi} from "../../services/api";

export default {
    name: "ControlPanel",
    data: () => ({
        classifiers: [],
    }),
    async mounted() {
        this.classifiers = await this.getClassifiersData()
    },
    methods: {
        async getClassifiersData() {
            const classifierData = await scorickApi.getClassifiers()
            return classifierData.data.data
        }
    }
}
</script>

<style scoped>

</style>
