from odoo import models, fields, api, exceptions

class MasterRuangan(models.Model):
    _name = 'master.ruangan'
    _description = 'Master Ruangan'

    nama_ruangan = fields.Char(required=True)
    tipe_ruangan = fields.Selection([
        ('kecil', 'Meeting Room Kecil'),
        ('besar', 'Meeting Room Besar'),
        ('aula', 'Aula')
    ], required=True)
    lokasi_ruangan = fields.Selection([
        ('1A', '1A'), ('1B', '1B'), ('1C', '1C'),
        ('2A', '2A'), ('2B', '2B'), ('2C', '2C')
    ], required=True)
    foto_ruangan = fields.Binary(required=True)
    kapasitas_ruangan = fields.Integer(required=True)
    keterangan = fields.Text()

class PemesananRuangan(models.Model):
    _name = 'pemesanan.ruangan'
    _description = 'Pemesanan Ruangan'

    nomor_pemesanan = fields.Char(string="Nomor Pemesanan", readonly=True)
    ruangan_id = fields.Many2one('master.ruangan', required=True)
    nama_pemesan = fields.Char(required=True)
    tanggal_pemesanan = fields.Date(required=True)
    status_pemesanan = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'On Going'),
        ('done', 'Done')
    ], default='draft')

    @api.constrains('nama_pemesan', 'ruangan_id', 'tanggal_pemesanan')
    def _check_unique_booking(self):
        if self.search([
            ('ruangan_id', '=', self.ruangan_id.id),
            ('tanggal_pemesanan', '=', self.tanggal_pemesanan),
            ('id', '!=', self.id)
        ]):
            raise exceptions.ValidationError("Ruangan sudah dipesan pada tanggal tersebut.")

        if self.search([('nama_pemesan', '=', self.nama_pemesan), ('id', '!=', self.id)]):
            raise exceptions.ValidationError("Nama pemesan sudah ada.")

    @api.model
    def create(self, vals):
        vals['nomor_pemesanan'] = self.env['ir.sequence'].next_by_code('pemesanan.ruangan') or '/'
        return super(PemesananRuangan, self).create(vals)

