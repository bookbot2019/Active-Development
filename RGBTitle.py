# BEWARE ALL YE WHO ENTER
# FOR HERE BE DRAGONS
"""
                              ______________                               
                        ,===:'.,            `-._                           
                             `:.`---.__         `-._                       
                              `:.     `--.         `.                     
                                 \.        `.         `.                   
                         (,,(,    \.         `.   ____,-`.,                
                      (,'     `/   \.   ,--.___`.'                         
                  ,  ,'  ,--.  `,   \.;'         `                         
                   `{D, {    \  :    \;                                    
                     V,,'    /  /    //                                    
                     j;;    /  ,' ,-//.    ,---.      ,                    
                     \;'   /  ,' /  _  \  /  _  \   ,'/                    
                           \   `'  / \  `'  / \  `.' /                     
                            `.___,'   `.__,'   `.__,' 
"""

class RGBTitle:
    def __init__(self, font, title_str, title_pos, colors):
        self.rendered_texts = []
        self.rendered_rects = []
        # title_str = 'Tetris'
        # title_pos = (100, 100)

        if(len(colors) != len(title_str)):
            raise ValueError("Color list is different length than title string")

        for idx, c in enumerate(colors):
            new_text = font.render(title_str[idx], True, c)
            new_rect = new_text.get_rect()
            new_rect.x = title_pos[0] + 24 * idx
            new_rect.y = title_pos[1]
            self.rendered_texts.append(new_text)
            self.rendered_rects.append(new_rect)
    
    def render(self, surface):
        for idx, t in enumerate(self.rendered_texts):
            surface.blit(t, self.rendered_rects[idx])