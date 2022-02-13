<template>
    <div>
        <v-navigation-drawer app
                             v-model=showNavigation
                             :mobile-breakpoint=mobileBreakpoint
                             class="pt-4"
        >
            <v-list-item>
                <v-btn to="/home/about">Informace</v-btn>
            </v-list-item>
            <v-list-item>
                <v-btn to="/home/anamnesis">Moje anamnéza</v-btn>
            </v-list-item>
            <v-list-item>
                <v-btn to="/home/current-illness">Aktuální onemocnění</v-btn>
            </v-list-item>
            <v-list-item class="mt-12">
                <v-btn to="/">Odhlásit</v-btn>
            </v-list-item>
        </v-navigation-drawer>

        <v-toolbar app v-if=showToolbar width="100%">
            <v-app-bar-nav-icon @click.stop="showNavigation = !showNavigation"></v-app-bar-nav-icon>
            <v-toolbar-title>Menu</v-toolbar-title>
        </v-toolbar>

        <v-main>
            <v-container fluid>
                <v-card class="pa-8">
                    <router-view></router-view>
                </v-card>
            </v-container>
        </v-main>
    </div>
</template>

<script>
    export default {
        data: function () {
            return {
                showNavigation: null,
                showToolbar: false,
                mobileBreakpoint: 1024
            }
        },
        methods: {
            isOnMobile() {
                return window.innerWidth < this.mobileBreakpoint;
            },
            updateLayout() {
                const onMobile = this.isOnMobile();
                // this.showNavigation = !onMobile;
                this.showToolbar = onMobile;
            }
        },
        destroyed() {
            removeEventListener('resize', this.updateLayout);
        },
        mounted() {
            addEventListener('resize', this.updateLayout);
        }
    }
</script>

<style>

</style>
