<template>
    <v-app>
        <Header></Header>

        <v-main class="grey lighten-3">
            <v-container class="mt-10">
                <v-row>
                    <ControlPanel></ControlPanel>

                    <v-col>
                        <v-sheet
                            min-height="70vh"
                            rounded="lg"
                        >
                            <router-view></router-view>
                        </v-sheet>
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
import Header from "@/components/Header";
import ControlPanel from "@/components/ControlPanel";

export default {
    name: 'App',

    components: {
        ControlPanel, Header
    },

    data: () => ({
        //
    }),
};
</script>

