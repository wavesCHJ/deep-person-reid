import torchreid


def _parse_data_for_train(data):
    imgs = data[0]
    pids = data[1]
    return imgs, pids

# Load data manager
datamanager = torchreid.data.ImageDataManager(
    root='reid-data',
    sources='market1501',
    targets='market1501',
    height=256,
    width=128,
    batch_size_train=32,
    batch_size_test=100,
    transforms=['random_flip', 'random_crop']
)

cnt = 0
num_batches = len(datamanager.trainloader)
for batch_idx, data in enumerate(datamanager.trainloader):

    imgs, pids = _parse_data_for_train(data)
    print("imgs:", imgs, "---pids:", pids)
    cnt = cnt + 1
    if cnt == 10:
        break

'''
# Build model, optimizer and lr_scheduler
model = torchreid.models.build_model(
    name='resnet50',
    num_classes=datamanager.num_train_pids,
    loss='softmax',
    pretrained=True
)

model = model.cuda()

optimizer = torchreid.optim.build_optimizer(
    model,
    optim='adam',
    lr=0.0003
)

scheduler = torchreid.optim.build_lr_scheduler(
    optimizer,
    lr_scheduler='single_step',
    stepsize=20
)

# Build engine
engine = torchreid.engine.ImageSoftmaxEngine(
    datamanager,
    model,
    optimizer=optimizer,
    scheduler=scheduler,
    label_smooth=True
)

# Run training and test
engine.run(
    save_dir='log/resnet50',
    max_epoch=60,
    eval_freq=10,
    print_freq=10,
    test_only=False
)
'''