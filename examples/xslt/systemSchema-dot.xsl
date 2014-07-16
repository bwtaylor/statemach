<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:sys="http://docs.rackspace.com/core/system/schema"
    version="1.0">

    <xsl:output method="text"/>

    <xsl:template match="/">
digraph SystemModel { rankdir=LR; fontname="Helvetica"; labelloc=b;
                    node [fontname="Helvetica", shape=ellipse, style=filled,fillcolor="#EEEEEE"]

           {
           rank=source
           Start
           }
           {
           <xsl:apply-templates/>
           }
           Start[label="", shape="point"]
           End[label="", shape="doublecircle", fillcolor="white"]
    }
    </xsl:template>
    <xsl:template match="sys:transition">
        <xsl:variable name="label">
            <xsl:text> [label="</xsl:text>
            <xsl:value-of select='@name'/>
            <xsl:text>"</xsl:text>
            <xsl:if test="@actor = 'SYSTEM'">
                <xsl:text>, color=red, fontcolor=red</xsl:text>
            </xsl:if>
            <xsl:text>];&#xa;</xsl:text>
        </xsl:variable>
        <xsl:value-of select="concat(@from,'->',@to,$label)"/>
    </xsl:template>
    <xsl:template match="text()"/>
</xsl:stylesheet>
