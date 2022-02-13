<template>
    <div>
        <h1>Zaznamenejte léky, které užíváte</h1>

        <prev-next-button prev="/home/anamnesis/personal" next="/home/anamnesis/social"></prev-next-button>
    </div>
</template>

<script>
    import PrevNextButton from "../misc/PrevNextButton";

    export default {
        components: {PrevNextButton}
    }
</script>
