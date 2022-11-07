<template>
    <div id="top-card">
        <TypeMessage></TypeMessage>
        <ChangePrice></ChangePrice>
        <ChangeStyle></ChangeStyle>
        <FontSize></FontSize>
        <ListChange></ListChange>
    </div>
</template>

<script>
import ChangeStyle from './ChangeStyle.vue';
import FontSize from './FontSize.vue';
import ListChange from './ListChange.vue';
import TypeMessage from './TypeMessage.vue';
import ChangePrice from './ChangePrice.vue';
export default {

    name: "HomeBase",
    components: {
        TypeMessage,
        ChangePrice,
        ListChange,
        FontSize,
        ChangeStyle,
    }
}
</script>