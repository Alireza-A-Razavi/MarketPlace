<template>
	<div id="index" class='mainItemPerPage'>
		<div id="topOfIndex">
			<div id="topOfIndexWrapper">
				<categorie></categorie>
				<slider></slider>	
			</div>			
		</div>
		<flip-card></flip-card>
		<div id="allCards">
			<card cardTitle="بیشترین کلیک شده" descs='فلان لان فلان خیلی فلا هی فلان بازم فلان' :products='getProducts()'></card>
		</div>
	</div>
</template>

<style>
	#topOfIndex{
		background: #d3d3d3;
	}
	#topOfIndexWrapper{
		display:flex;
		justify-content: center;
		widTH:100%;
		padding:20px;
	}
	#index{
		position: relative;
	}
	#allCards{
		display: flex;
		width:100% ;
		flex-direction: column;
		align-items: center;
	}
	#mostClicked{

		grid-area: mostClicked;
	}
	#slider{
		grid-area: slide
	}
	#new{
		grid-area: new;
	}

	#app{
		display: grid;
		width: 100%;
		grid-template-columns: repeat(2,1fr);
		grid-template-rows: fit-content(1000rem) auto auto auto fit-content(1000rem);
		grid-template-areas: 
		'header header'
		'slicer slicer'
		'navigation navigation'
		'main main'
		'footer footer'
	}
	.titleCard{
		display: flex;
		justify-content: center;
	}


	#index{
			display: flex;
			flex-direction: column;
			align-items: center;

		}

	#flatMenu{
		grid-area: flatMenu
	}


	.singleCard{
		background: white;
	}

	#footer{
		grid-area: footer
	}
	.hamCats{
		grid-area:hamCats
	}
	@media (max-width:924px)
	{
		#slider{
			width:100%;

		}
		#sideSliderCats{
			display:none
		}
	}


</style>


<script>
	import slider from "./slider/slider.vue"
	import card from './card/card.vue'
	import flipCard from './flipCard/flipCard.vue'
	import categorie from './categorie/categorie.vue'
	export default{
		components:{
			slider,
			card,
			categorie,
			flipCard
		},
		data(){
			return{
				products:[{desc:'محصل فلاkmfkdmfkdmsfkmfkmfkdm kmk kfmdk mkfmksdm kmf kdsن و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"}]
			}
		},
		methods:{
			getProducts(){
				return JSON.stringify(this.products)
			}
		}
		
	}
</script>