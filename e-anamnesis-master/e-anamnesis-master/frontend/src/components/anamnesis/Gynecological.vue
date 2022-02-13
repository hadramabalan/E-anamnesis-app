<template>
    <div>
        <h1>Vyplňte informace o gynekologickém stavu</h1>

        <prev-next-button prev="/home/anamnesis/allergies" next="/home/anamnesis/final"></prev-next-button>
    </div>
</template>

<script>
    import PrevNextButton from "../misc/PrevNextButton";

    export default {
        components: {PrevNextButton}
    }
</script>
