<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.10" tiledversion="1.10.2" name="event" tilewidth="16" tileheight="16" tilecount="16" columns="8">
 <image source="../png/event.png" trans="fff568" width="128" height="32"/>
 <tile id="0">
  <properties>
   <property name="collides" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="1">
  <properties>
   <property name="collides" type="bool" value="true"/>
   <property name="event" value="surf"/>
  </properties>
 </tile>
 <tile id="2">
  <properties>
   <property name="light" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="3">
  <properties>
   <property name="spawn" value="land"/>
  </properties>
 </tile>
 <tile id="4">
  <properties>
   <property name="spawn" value="water"/>
  </properties>
 </tile>
</tileset>
