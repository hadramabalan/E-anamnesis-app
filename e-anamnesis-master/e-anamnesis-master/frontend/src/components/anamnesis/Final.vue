<template>
    <div>
        <h1>Hotovo</h1>

        <prev-next-button prev="/home/anamnesis/gynecological" next="/home" :on-next="commit"></prev-next-button>
    </div>
</template>

<script>
    import PrevNextButton from "../misc/PrevNextButton";
    export default {
        components: {PrevNextButton},
        methods: {
            commit() {
                console.log("Dokončeno!");
            }
        }
    }
</script>
