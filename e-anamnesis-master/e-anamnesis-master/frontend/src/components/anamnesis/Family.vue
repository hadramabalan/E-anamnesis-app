<template>
    <div>
        <h1>Vyplňte údaje o své rodině</h1>

        <prev-next-button prev="/home/anamnesis" next="/home/anamnesis/personal"></prev-next-button>
    </div>
</template>

<script>
    import PrevNextButton from "../misc/PrevNextButton";
    export default {
        components: {PrevNextButton}
    }
</script>
