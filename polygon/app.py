import xml.etree.ElementTree as ET

class ConvertToBB:
    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()

    def extrair_pontos_from_polygon(self, polygon_tag):
        points_str = polygon_tag.attrib['points']
        pontos = [tuple(map(float, p.split(','))) for p in points_str.split(';')]
        return pontos

    def converter_polygon_to_bb(self, pontos):
        x_values = [p[0] for p in pontos]
        y_values = [p[1] for p in pontos]

        xtl = min(x_values)
        ytl = min(y_values)
        xbr = max(x_values)
        ybr = max(y_values)

        return (xtl, ytl, xbr, ybr)

    def converter_e_substituir(self):
        for image_tag in self.root.findall('image'):
            polygons = image_tag.findall('polygon')
            for polygon_tag in polygons:
                pontos = self.extrair_pontos_from_polygon(polygon_tag)
                bbox = self.converter_polygon_to_bb(pontos)
                
                # Criando uma nova tag <box> com os valores da bounding box
                box_tag = ET.Element('box')
                box_tag.set('label', polygon_tag.attrib['label'])
                box_tag.set('source', 'Ground truth')
                box_tag.set('occluded', polygon_tag.attrib['occluded'])
                box_tag.set('xtl', str(bbox[0]))
                box_tag.set('ytl', str(bbox[1]))
                box_tag.set('xbr', str(bbox[2]))
                box_tag.set('ybr', str(bbox[3]))
                box_tag.set('z_order', polygon_tag.attrib['z_order'])
                
                # Substituindo a tag <polygon> pela nova tag <box>
                image_tag.remove(polygon_tag)
                image_tag.append(box_tag)

    def salvar_novo_xml(self, output_file):
        self.tree.write(output_file)

# Exemplo de uso da classe
caminho_arquivo_xml = 'annotations.xml'
converter = ConvertToBB(caminho_arquivo_xml)
converter.converter_e_substituir()
converter.salvar_novo_xml(caminho_arquivo_xml.replace('.xml', '_bbox.xml'))
