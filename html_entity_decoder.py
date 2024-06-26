"""
################################################################################
#                                                                              #
# This code was created by veilwr4ith                                          #
#                                                                              #
# HTML Entity Decoder                                                          #
#                                                                              #
################################################################################
"""

import html

def html_entity_decoder(text):
    decoded_text = html.unescape(text)
    return decoded_text

html_entity = input("Enter the HTML Entity: ")
decoded_entity = html_entity_decoder(html_entity)
print("-" * 30)
print("Decoded Entity: ", decoded_entity)
