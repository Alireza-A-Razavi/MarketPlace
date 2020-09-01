<template>
    <div id="mapid">
        
    </div>

</template>

<script>
    import { GeoSearchControl, OpenStreetMapProvider } from 'leaflet-geosearch';
    export default{
        mounted(){
            
            try{
                const provider = new OpenStreetMapProvider();

                const searchControl = new GeoSearchControl({
                    provider: provider,
                });   
                var mymap = L.map('mapid').setView([32.54681317351517 ,53.50428547330944], 5);
                
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom:19,
                    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                }).addTo(mymap);
                mymap.addControl(searchControl);
                let allMarkers=L.marker([0,0]).addTo(mymap)
                mymap.on('click', function(e){
                    var coord = e.latlng;
                    var lat = coord.lat;
                    var lng = coord.lng;
                    console.log(lat,lng)
                    
                    allMarkers.setLatLng([lat,lng])
                });
                document.querySelector("input.glass").setAttribute("placeholder",'جست و جوی ادرس')
            }catch(err)
            {
                console.log(err)
            }               
        }
    }

</script>

<style>
    #mapid{
        height:500px;
        width:90%;
        margin:auto;
        margin-top:20px;
    }
    .leaflet-top.leaflet-left{
        display: flex;
        flex-direction: column;
        widtH:95%;
        position: relative;
        top: -12px;
    }
    .leaflet-control-zoom.leaflet-bar.leaflet-control{
        order:2;
        max-width:max-content
    }
    input.glass{
        width:100%;
        color:black;

    }

    .geosearch.leaflet-bar.leaflet-control.leaflet-control-geosearch.leaflet-geosearch-button{
        background-color: rgb(179, 171, 171) !important;
        font-size:12pt !important;
        overflow: auto;
    }
    .results.active div{
        text-align:right;
        font-size:12pt
    }
</style>