<template>
    <div>
        <v-row>
            <v-col class="col-8">
                <router-view></router-view>
            </v-col>
            <v-col v-if="isEditing" class="col-4">
                <v-stepper
                        v-model="s"
                        vertical
                >
                    <template v-for="step in steps">
                        <v-stepper-step
                                :key="step.key"
                                :step="step.key"
                                editable
                                @click.stop="goTo(step.key)"
                        >
                            {{step.name}}
                        </v-stepper-step>
                        <v-stepper-content :key="'A' + step.key" :step="step.key"></v-stepper-content>
                    </template>
                </v-stepper>
            </v-col>
        </v-row>
    </div>
</template>

<script>
    import anamnesisSteps from "../../data";

    export default {
    data () {
        return {
            // Active step key
            s: 0,
            steps: [],
            isEditing: false,
        }
    },
    mounted() {
        this.mapAnamnesisRoutesIntoSteps();
    },
    methods: {
        goTo(key) {
            const thisStep = this.getStepByKey(key);
            if (thisStep.path !== this.getCurrentPathLastPart())
                this.$router.push(`/home/anamnesis/${thisStep.path}`);
        },
        getAnamnesisRoutes() {
            const homeRoutes = this.getChildRoutes(this.$router.options.routes, '/home');
            return this.getChildRoutes(homeRoutes, 'anamnesis');
        },
        getChildRoutes(routes, path) {
            for (let i = 0; i < routes.length; i++) {
                if (routes[i].path === path) {
                    return routes[i].children
                }
            }
            return []
        },
        getStepByKey(key) {
            for (let i = 0; i < this.steps.length; i++) {
                if (this.steps[i].key === key) return this.steps[i];
            }
        },
        mapAnamnesisRoutesIntoSteps() {
            const routes = this.getAnamnesisRoutes();
            routes.forEach(route => {
                // TODO -> how to handle final step?
                if (route.path.length !== 0 && route.path !== 'final') {
                    const stepName = anamnesisSteps.get(route.path);
                    this.steps.push({
                        key: stepName[0],
                        name: stepName,
                        path: route.path
                    })
                }
            })
        },
        getCurrentPathLastPart() {
            const path = this.$route.path.split('/');
            return path[path.length - 1].toLowerCase();
        }
    },
    watch: {
        $route() {
            const mostPath = this.getCurrentPathLastPart();

            this.steps.forEach(step => {
                if (step.path === mostPath) {
                    this.s = step.key;
                }
            });
            this.isEditing = !!anamnesisSteps.get(mostPath);
        }
    }
}
</script>
