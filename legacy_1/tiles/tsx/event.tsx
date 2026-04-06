<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.10" tiledversion="1.10.2" name="event" tilewidth="16" tileheight="16" tilecount="21" columns="7">
 <editorsettings>
  <export target="../json/outdoor/event.json" format="json"/>
 </editorsettings>
 <image source="../png/event.png" trans="fff568" width="112" height="48"/>
 <tile id="0">
  <properties>
   <property name="collides" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="1">
  <properties>
   <property name="light" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="2">
  <properties>
   <property name="spawn" value="water"/>
   <property name="type" value="water_1"/>
  </properties>
 </tile>
 <tile id="3">
  <properties>
   <property name="spawn" value="water"/>
   <property name="type" value="water_2"/>
  </properties>
 </tile>
 <tile id="4">
  <properties>
   <property name="spawn" value="land"/>
   <property name="type" value="snow_1"/>
  </properties>
 </tile>
 <tile id="5">
  <properties>
   <property name="spawn" value="land"/>
   <property name="type" value="sand_1"/>
  </properties>
 </tile>
 <tile id="6">
  <properties>
   <property name="spawn" value="land"/>
  </properties>
 </tile>
 <tile id="7">
  <properties>
   <property name="spawn" value="land"/>
   <property name="type" value="grass_1"/>
  </properties>
 </tile>
 <tile id="8">
  <properties>
   <property name="spawn" value="land"/>
   <property name="type" value="grass_2"/>
  </properties>
 </tile>
 <tile id="9">
  <properties>
   <property name="spawn" value="land"/>
   <property name="type" value="grass_3"/>
  </properties>
 </tile>
 <tile id="10">
  <properties>
   <property name="spawn" value="land"/>
   <property name="type" value="grass_4"/>
  </properties>
 </tile>
 <tile id="11">
  <properties>
   <property name="spawn" value="land"/>
   <property name="type" value="grass_5"/>
  </properties>
 </tile>
 <tile id="12">
  <properties>
   <property name="spawn" value="land"/>
   <property name="type" value="grass_6"/>
  </properties>
 </tile>
 <tile id="13">
  <properties>
   <property name="spawn" value="land"/>
   <property name="type" value="grass_7"/>
  </properties>
 </tile>
 <tile id="14">
  <properties>
   <property name="collides" type="bool" value="true"/>
   <property name="event" value="surf"/>
  </properties>
 </tile>
</tileset>
