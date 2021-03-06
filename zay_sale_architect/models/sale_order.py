# -*- coding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2016 - Leandro Augusto  <leandro@leandroaugusto.eti.br>       #
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).               #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU Affero General Public License for more details.                         #
#                                                                             #
# You should have received a copy of the GNU Affero General Public License    #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
###############################################################################

from openerp import models, fields, api

class SaleOrderArchitect(models.Model):
    _inherit = 'sale.order'

    #architect_id = fields.Many2one('res.partner', domain="[('isArchitect', '=', '1')]")
    architect_id = fields.Many2one( comodel_name="res.partner", string="Arquiteto",
                                    domain="[('isArchitect', '=', '1')]" )
