# ############################################################
# Importing - Same For All Render Layer Tests
# ############################################################

import unittest
import os
import sys

from render_layer_common import *


# ############################################################
# Testing
# ############################################################

class UnitTesting(MoveLayerCollectionTesting):
    def get_reference_scene_tree_map(self):
        # original tree, no changes
        return self.get_initial_scene_tree_map()

    def get_reference_layers_tree_map(self):
        # original tree, no changes
        return self.get_initial_layers_tree_map()

    def test_layer_collection_move_a(self):
        """
        Test outliner operations
        """
        self.setup_tree()
        self.assertFalse(self.move_below('Layer 1.3.cat', 'Layer 1.3.dog'))
        self.compare_tree_maps()

    def test_layer_collection_move_b(self):
        """
        Test outliner operations
        """
        self.setup_tree()
        self.assertFalse(self.move_above('Layer 1.3.dog', 'Layer 1.3.cat'))
        self.compare_tree_maps()


# ############################################################
# Main - Same For All Render Layer Tests
# ############################################################

if __name__ == '__main__':
    UnitTesting._extra_arguments = setup_extra_arguments(__file__)
    unittest.main()
