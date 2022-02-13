<template>
    <div>
        <v-form class="mb-4">
            <p>Máte bolesti</p>
            <v-radio-group v-model="ache" row>
                <v-radio
                        label="Ano"
                        value="ache-true"
                        @click.stop="showAcheForm"
                ></v-radio>
                <v-radio
                        label="Ne"
                        value="ache-false"
                        @click.stop="hideAcheForm"
                ></v-radio>
            </v-radio-group>

            <div v-if="shouldShowAcheForm">
                <v-text-field
                        v-model="acheLocation"
                        label="Kde máte bolesti?"
                ></v-text-field>

                <p>Bolest je</p>
                <v-radio-group v-model="acheType" row>
                    <v-radio label="Tlaková"></v-radio>
                    <v-radio label="Bodavá"></v-radio>
                    <v-radio label="Svíravá"></v-radio>
                    <v-radio label="Řezavá"></v-radio>
                </v-radio-group>

                <v-text-field
                        v-model="acheDuration"
                        label="Jak dlouho bolest trvá (počet hodin)"
                ></v-text-field>

                <p>Intezita bolesti</p>
                <v-radio-group row>
                    <v-radio label="0"></v-radio>
                    <v-radio label="1–2"></v-radio>
                    <v-radio label="2–4"></v-radio>
                    <v-radio label="3–6"></v-radio>
                    <v-radio label="4–8"></v-radio>
                    <v-radio label="5–10"></v-radio>
                </v-radio-group>
            </div>

            <v-row class="mb-2">
                <v-col class="col-2">
                    <v-btn color="primary" @click="share">Sdílet</v-btn>
                </v-col>
                <v-col class="col-10">
                    <p>{{shareCode}}</p>
                </v-col>
            </v-row>

            <div>
                <v-btn @click="goBack" color="primary" class="ma-2" outlined>Zpět</v-btn>
                <v-btn @click="commitIllness" color="primary" class="ma-2">Dokončit</v-btn>
            </div>
        </v-form>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                ache: null,
                acheLocation: null,
                acheType: null,
                acheDuration: null,
                acheIntensity: null,

                shouldShowAcheForm: false,

                shareCode: ""
            }
        },
        methods: {
            share() {
                if (this.shareCode.length === 0)
                    this.shareCode = "1650106801";
                else
                    this.shareCode = ""
            },
            showAcheForm() {
                this.shouldShowAcheForm = true;
            },
            hideAcheForm() {
                this.shouldShowAcheForm = false;
            },
            commitIllness() {
                // this.$router.push('/home/current-illness');
            },
            goBack() {
                this.$router.push('/home/current-illness');
            }
        }
    }
</script>
