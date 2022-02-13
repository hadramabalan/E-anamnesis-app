<template>
    <div>
        <v-app-bar app>
            <v-toolbar-title>eAnamnéza</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn to="/home" text large>Přihlásit</v-btn>
        </v-app-bar>

        <v-main>
            <v-container class="mt-xs-4 mt-12">
                <v-row>
                    <v-col class="col-lg-4 col-sm-12">
                        <v-card class="mb-12" flat>
                            <v-card-title class="text-word-break text-xs-h1 text-sm-h2 text-md-h2 text-lg-h2">
                                Snadný a bezpečný způsob, jak sdílet data se svými lékaři
                            </v-card-title>

                            <v-card-subtitle class="text-h5 mt-4 mb-6">
                                Mějte informace o zdravotním stavu přehledně na jednom místě.
                            </v-card-subtitle>

                            <div class="text-center">
                                <v-btn to="/home" class="ma-2" color="primary" x-large outlined>Přihlásit</v-btn>
                                <v-btn class="ma-2" color="primary" x-large>Vytvořit účet</v-btn>
                            </div>
                        </v-card>
                    </v-col>
                    <v-col class="col-lg-8 col-sm-12">
                        <v-card flat>
                            <v-img
                                    src="https://images.unsplash.com/photo-1579684385127-1ef15d508118?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1000&q=80"
                                    lazy-src="https://images.unsplash.com/photo-1579684385127-1ef15d508118?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=100&q=80"
                            >
                                <template v-slot:placeholder>
                                    <v-row
                                            class="fill-height ma-0"
                                            align="center"
                                            justify="center"
                                    >
                                        <v-progress-circular
                                                indeterminate
                                                color="grey lighten-5"
                                        ></v-progress-circular>
                                    </v-row>
                                </template>
                            </v-img>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </div>
</template>

<script>
    export default {

    }
</script>

<style>
    .text-xs-h1 {
        font-size: xx-large;
    }

    .text-word-break {
        word-break: normal;
    }
</style>
