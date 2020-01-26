from django.db import models


class PeerType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ServiceType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class internetIP(models.Model):
    name = models.CharField(max_length=100)
    ip = models.GenericIPAddressField(null=True)

    def __str__(self):
        return self.name


class coreIP(models.Model):
    name = models.CharField(max_length=100)
    ip = models.GenericIPAddressField(null=True)

    def __str__(self):
        return self.name


class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField('Estatus', default=True)
    created_at = models.DateField(
        'Fecha de Creación', auto_now=False, auto_now_add=True)
    updated_at = models.DateField(
        'Fecha de Actualización', auto_now=True, auto_now_add=False)
    deleted_at = models.DateField(
        'Fecha de Elminación', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class internetInterface(ModelBase):
    device = models.CharField('Nombre del equipo', max_length=100)
    port = models.CharField('Puerto', max_length=200)
    description = models.CharField('Descripción', max_length=200, null=True)
    peerType = models.ForeignKey(PeerType, on_delete=models.CASCADE, null=True)
    gbpsrx = models.FloatField('Gbps RX',)
    gbpstx = models.FloatField('Gbps TX',)
    gbpsmax = models.FloatField('Gbps MAX',)
    capacityInterface = models.FloatField('Capacidad', default='0')
    utilization = models.FloatField('Utilización', default='0')
    utilizationrx = models.FloatField('Utilización RX', default='0')
    utilizationtx = models.FloatField('Utilización TX', default='0')
    increase = models.FloatField('Crecimiento', null=True)
    bpsTime = models.DateTimeField('Fecha', null=True)
    solutionTime = models.DateField('Fecha de Solución', null=True)
    comment = models.TextField('Comentarios', null=True)
    nameServices = models.ManyToManyField(Service)
    deviceIndex = models.CharField('Equipo_Puerto', max_length=200)

    class Meta:
        verbose_name: 'internetInterface'
        verbose_name_plural: 'internetInterfaces'

    def __str__(self):
        return '{0},{1}'.format(self.device, self.port)


class coreInterface(ModelBase):
    device = models.CharField('Nombre del equipo', max_length=100)
    port = models.CharField('Puerto', max_length=200)
    description = models.CharField('Descripción', max_length=200, null=True)
    serviceType = models.ForeignKey(
        ServiceType, on_delete=models.CASCADE, null=True)
    gbpsrx = models.FloatField('Gbps RX',)
    gbpstx = models.FloatField('Gbps TX',)
    gbpsmax = models.FloatField('Gbps MAX',)
    capacityInterface = models.FloatField('Capacidad', default='0')
    utilization = models.FloatField('Utilización', default='0')
    utilizationrx = models.FloatField('Utilización RX', default='0')
    utilizationtx = models.FloatField('Utilización TX', default='0')
    increase = models.FloatField('Crecimiento', null=True)
    bpsTime = models.DateTimeField('Fecha', null=True)
    solutionTime = models.DateField('Fecha de Solución', null=True)
    comment = models.TextField('Comentarios', null=True)
    nameServices = models.ManyToManyField(Service)
    deviceIndex = models.CharField('Equipo_Puerto', max_length=200)

    class Meta:
        verbose_name: 'coreInterface'
        verbose_name_plural: 'coreInterfaces'

    def __str__(self):
        return '{0},{1}'.format(self.device, self.port)
