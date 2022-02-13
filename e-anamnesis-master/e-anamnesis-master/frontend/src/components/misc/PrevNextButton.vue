<template>
    <v-row class="mt-8">
        <v-btn :to="prev" class="ma-1">Zpět</v-btn>
        <v-btn :to="next" @click="onNext" class="ma-1">Další</v-btn>
    </v-row>
</template>

<script>
    export default {
        props: {
            prev: String,
            next: String,
            onNext: {
                default: function () {},
                type: Function
            }
        }
    }
</script>
